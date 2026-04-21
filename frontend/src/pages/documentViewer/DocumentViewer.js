// eslint-disable-next-line
import { useEffect, useState } from "react";
import { Viewer } from "@react-pdf-viewer/core";
import { defaultLayoutPlugin } from "@react-pdf-viewer/default-layout";
import { useSearchParams } from "react-router-dom";

import "@react-pdf-viewer/core/lib/styles/index.css";
import "@react-pdf-viewer/default-layout/lib/styles/index.css";

import "./DocumentViewer.css";
import Header from "../component/header/Header";

import * as pdfjs from "pdfjs-dist";
pdfjs.GlobalWorkerOptions.workerSrc =
  `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.js`;

const STATUS_LABELS = {
  covered: { label: "Covered", color: "#1a7f4b" },
  not_covered: { label: "Not Covered", color: "#c0392b" },
  related: { label: "Related", color: "#7f6d17" },
};

const CODE_TYPES = ["CPT", "HCPCS", "ICD-10"];

const renderPage = (props) => (
  <>
    {props.canvasLayer.children}
    <div style={{ userSelect: "none" }}>{props.textLayer.children}</div>
    {props.annotationLayer.children}
  </>
);

const DocumentViewer = () => {
  const [searchParams] = useSearchParams();
  const coverageId = searchParams.get("id");

  const [details, setDetails] = useState(null);
  const [activeTab, setActiveTab] = useState("covered");
  const [typeFilter, setTypeFilter] = useState(null);
  const [codeSearch, setCodeSearch] = useState("");

  const defaultLayoutPluginInstance = defaultLayoutPlugin();

  useEffect(() => {
    if (!coverageId) return;
    fetch(`http://localhost:8000/policy-coverages/${coverageId}/details`)
      .then((r) => r.ok ? r.json() : null)
      .then(setDetails)
      .catch(() => setDetails(null));
  }, [coverageId]);

  const fileUrl = details?.document_url
    ? `http://localhost:8000/${details.document_url.split("/").map(encodeURIComponent).join("/")}`
    : null;

  const codesByStatus = details?.codes?.reduce((acc, c) => {
    const key = c.coverage_status;
    if (!acc[key]) acc[key] = [];
    acc[key].push(c);
    return acc;
  }, {}) ?? {};

  const tabs = Object.keys(STATUS_LABELS).filter((s) => codesByStatus[s]?.length);

  const visibleCodes = (codesByStatus[activeTab] ?? []).filter((c) => {
    const matchesType = !typeFilter || c.code_type === typeFilter;
    const q = codeSearch.toLowerCase();
    const matchesSearch = !q ||
      c.code.toLowerCase().includes(q) ||
      c.description.toLowerCase().includes(q);
    return matchesType && matchesSearch;
  });

  const toggleType = (t) => setTypeFilter((prev) => prev === t ? null : t);

  return (
    <>
      <Header />
      <div className="layout">

        <aside className="sidebar">
          {details ? (
            <>
              <div className="meta">
                <h3 className="title">{details.description}</h3>
                <div className="tags">
                  <span className="tag provider">{details.provider_name}</span>
                  <span className="tag policy">{details.policy_name}</span>
                </div>
                <div className="info-row">
                  <span className="info-label">Coverage period</span>
                  <span className="info-value">
                    {details.start_date} &ndash; {details.end_date}
                  </span>
                </div>
                {details.link_to_original && (
                  <a
                    className="source-link"
                    href={details.link_to_original}
                    target="_blank"
                    rel="noreferrer"
                  >
                    View original source ↗
                  </a>
                )}
              </div>

              {tabs.length > 0 && (
                <div className="codes-section">
                  <p className="codes-heading">Associated Codes</p>

                  <div className="tabs">
                    {tabs.map((s) => (
                      <button
                        key={s}
                        className={`tab ${activeTab === s ? "active" : ""}`}
                        style={activeTab === s ? { borderBottomColor: STATUS_LABELS[s].color, color: STATUS_LABELS[s].color } : {}}
                        onClick={() => setActiveTab(s)}
                      >
                        {STATUS_LABELS[s].label}
                        <span className="tab-count">{codesByStatus[s].length}</span>
                      </button>
                    ))}
                  </div>

                  <div className="type-filters">
                    {CODE_TYPES.map((t) => (
                      <button
                        key={t}
                        className={`type-btn ${typeFilter === t ? "active" : ""}`}
                        onClick={() => toggleType(t)}
                      >
                        {t}
                      </button>
                    ))}
                  </div>

                  <input
                    className="code-search"
                    type="text"
                    placeholder="Search code or description…"
                    value={codeSearch}
                    onChange={(e) => setCodeSearch(e.target.value)}
                  />

                  <div className="codes-list">
                    {visibleCodes.length === 0 ? (
                      <p className="no-codes">No codes match your filter.</p>
                    ) : (
                      visibleCodes.map((c, i) => (
                        <div key={i} className="code-row">
                          <span className="code-badge">{c.code_type}</span>
                          <span className="code-value">{c.code}</span>
                          <span className="code-desc">{c.description}</span>
                        </div>
                      ))
                    )}
                  </div>
                </div>
              )}
            </>
          ) : (
            <p className="no-details">No details available.</p>
          )}
        </aside>

        <div className="viewer">
          {fileUrl ? (
            <Viewer
              fileUrl={fileUrl}
              renderPage={renderPage}
              plugins={[defaultLayoutPluginInstance]}
            />
          ) : (
            <div className="no-doc">No document selected.</div>
          )}
        </div>

      </div>
    </>
  );
};

export default DocumentViewer;
