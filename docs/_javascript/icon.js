SVG_NAMESPACE = "http://www.w3.org/2000/svg";
FONTAWESOME_COMMENT =
  "Font Awesome Pro 6.2.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc.";
const LINK_CSS_CLASS = {
  EXTERNAL: "external-link",
  MAILTO: "mailto-link",
  DOWNLOAD: "download-link",
};
const SVG_CONTENT = {
  "external-link": {
    comment: FONTAWESOME_COMMENT,
    viewBox: "0 0 448 512",
    path: "M288 32c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9L306.7 128 169.4 265.4c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L352 173.3l41.4 41.4c9.2 9.2 22.9 11.9 34.9 6.9s19.8-16.6 19.8-29.6V64c0-17.7-14.3-32-32-32H288zM80 64C35.8 64 0 99.8 0 144V400c0 44.2 35.8 80 80 80H336c44.2 0 80-35.8 80-80V320c0-17.7-14.3-32-32-32s-32 14.3-32 32v80c0 8.8-7.2 16-16 16H80c-8.8 0-16-7.2-16-16V144c0-8.8 7.2-16 16-16h80c17.7 0 32-14.3 32-32s-14.3-32-32-32H80z",
  },
  "mailto-link": {
    comment: FONTAWESOME_COMMENT,
    viewBox: "0 0 512 512",
    path: "M0 128C0 92.65 28.65 64 64 64H448C483.3 64 512 92.65 512 128V384C512 419.3 483.3 448 448 448H64C28.65 448 0 419.3 0 384V128zM48 128V150.1L220.5 291.7C241.1 308.7 270.9 308.7 291.5 291.7L464 150.1V127.1C464 119.2 456.8 111.1 448 111.1H64C55.16 111.1 48 119.2 48 127.1L48 128zM48 212.2V384C48 392.8 55.16 400 64 400H448C456.8 400 464 392.8 464 384V212.2L322 328.8C283.6 360.3 228.4 360.3 189.1 328.8L48 212.2z",
  },
  "download-link": {
    comment: FONTAWESOME_COMMENT,
    viewBox: "0 0 512 512",
    path: "M288 32c0-17.7-14.3-32-32-32s-32 14.3-32 32V274.7l-73.4-73.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l128 128c12.5 12.5 32.8 12.5 45.3 0l128-128c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L288 274.7V32zM64 352c-35.3 0-64 28.7-64 64v32c0 35.3 28.7 64 64 64H448c35.3 0 64-28.7 64-64V416c0-35.3-28.7-64-64-64H346.5l-45.3 45.3c-25 25-65.5 25-90.5 0L165.5 352H64zM432 456c-13.3 0-24-10.7-24-24s10.7-24 24-24s24 10.7 24 24s-10.7 24-24 24z",
  },
};

function addListenerMulti(element, eventNames, listener) {
  const events = eventNames.split(" ");
  for (let i = 0, iLen = events.length; i < iLen; i++) {
    element.addEventListener(events[i], listener, false);
  }
}

addListenerMulti(document, "DOMContentLoaded DOMContentSwitch", (event) => {
  const anchorElements = document.querySelectorAll(".md-content a");
  for (var i = 0; i < anchorElements.length; i++) {
    var anchorElement = anchorElements[i];
    if (!isLink(anchorElement)) {
      continue;
    }

    var linkCssClassName = getLinkCssClassName(anchorElement);
    if (!linkCssClassName) {
      continue;
    }
    modifyElement(
      document,
      linkCssClassName,
      SVG_CONTENT[linkCssClassName],
      anchorElement
    );
  }
});

function getLinkCssClassName(anchorElement) {
  if (isExternalLink(anchorElement)) {
    return LINK_CSS_CLASS.EXTERNAL;
  } else if (isMailtoLink(anchorElement)) {
    return LINK_CSS_CLASS.MAILTO;
  } else if (isDownloadLink(anchorElement)) {
    return LINK_CSS_CLASS.DOWNLOAD;
  }
}

function modifyElement(document, linkCssClassName, svgContent, anchorElement) {
  anchorElement.classList.add(linkCssClassName);
  var svgElement = createSvgElement(document, svgContent);
  anchorElement.insertBefore(svgElement, anchorElement.firstChild);
}

function isLink(anchorElement) {
  return (
    anchorElement.classList.contains("md-icon") !== true &&
    anchorElement.classList.contains("download-button") !== true
  );
}

function isExternalLink(anchorElement) {
  const isHypertextProtocol = ["http:", "https:"].includes(
    anchorElement.protocol
  );
  const isExternal = anchorElement.hostname !== window.location.hostname;
  return isHypertextProtocol && isExternal;
}

function isMailtoLink(anchorElement) {
  const isMailtoProtocol = anchorElement.protocol == "mailto:";
  return isMailtoProtocol;
}

function isDownloadLink(anchorElement) {
  const stem = anchorElement.pathname.split("/").pop();
  const hasDot = stem.includes(".");
  return hasDot;
}

function createSvgElement(document, svgContent) {
  var svgElement = document.createElementNS(SVG_NAMESPACE, "svg");
  svgElement.setAttributeNS(null, "viewBox", svgContent.viewBox);

  commentElement = document.createComment(svgContent.comment);
  svgElement.appendChild(commentElement);

  var pathElement = document.createElementNS(SVG_NAMESPACE, "path");
  pathElement.setAttributeNS(null, "d", svgContent.path);
  svgElement.appendChild(pathElement);

  return svgElement;
}
