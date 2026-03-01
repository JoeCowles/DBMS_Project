// eslint-disable-next-line
import { Viewer } from "@react-pdf-viewer/core";
import "@react-pdf-viewer/core/lib/styles/index.css";

import "./DocumentViewer.css";

import * as pdfjs from "pdfjs-dist";
pdfjs.GlobalWorkerOptions.workerSrc =
  `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.js`;

const renderPage = (props) => {
  return (
    <>
      {props.canvasLayer.children}

      <div style={{ userSelect: "none" }}>
        {props.textLayer.children}
      </div>

      {props.annotationLayer.children}
    </>
  );
};

const DocumentViewer = () => {
  return (
    <div className="viewer-container">
      <div className="viewer-inner">
        <Viewer
          fileUrl="./Sample.pdf"
          renderPage={renderPage}
        />
      </div>
    </div>
  );
};

export default DocumentViewer;
