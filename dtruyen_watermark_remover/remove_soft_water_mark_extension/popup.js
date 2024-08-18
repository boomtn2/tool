document.addEventListener('DOMContentLoaded', function() {
  // var helloButton = document.getElementById('helloButton');
  // helloButton.addEventListener('click', function() {
  //   chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
  //     chrome.tabs.executeScript(tabs[0].id, {
  //       code: 'var mainHeaderElement = document.getElementById("main-header"); if (mainHeaderElement) mainHeaderElement.remove(); var chapterContentElement = document.getElementById("chapter-content"); if (chapterContentElement) { chapterContentElement.style.webkitUserSelect = "unset"; var parentElement = chapterContentElement.parentNode; var siblingElements = Array.from(parentElement.children); siblingElements.forEach(function(sibling) { if (sibling !== chapterContentElement) parentElement.removeChild(sibling); }); } var breadcrumbElement = document.getElementById("breadcrumb"); if (breadcrumbElement) breadcrumbElement.remove();var maincmElement = document.querySelector(".maincm"); if (maincmElement) maincmElement.remove();var mainFooterElement = document.getElementById("main-footer"); if (mainFooterElement) mainFooterElement.remove();var chapterPageElement = document.getElementById("chapter-page"); if (chapterContentElement) { chapterPageElement.style.maxWidth = "none"; } var mainElement = document.getElementById("main"); if (mainElement) { mainElement.style.marginTop = "0"; } const canvasElements = document.querySelectorAll("canvas"); canvasElements.forEach((canvas) => { const h1 = document.createElement("h1"); h1.textContent = "==========================================================="; canvas.replaceWith(h1); });'
  //     });
  //   });
  // });
  
  var hiButton = document.getElementById('hiButton');
  
  hiButton.addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      chrome.tabs.executeScript(tabs[0].id, {
        code: 'var mainHeaderElement = document.getElementById("main-header"); if (mainHeaderElement) mainHeaderElement.remove(); var chapterContentElement = document.getElementById("chapter-content"); if (chapterContentElement) { chapterContentElement.style.webkitUserSelect = "unset"; var parentElement = chapterContentElement.parentNode; var siblingElements = Array.from(parentElement.children); siblingElements.forEach(function(sibling) { if (sibling !== chapterContentElement) parentElement.removeChild(sibling); }); } var breadcrumbElement = document.getElementById("breadcrumb"); if (breadcrumbElement) breadcrumbElement.remove();var maincmElement = document.querySelector(".maincm"); if (maincmElement) maincmElement.remove();var mainFooterElement = document.getElementById("main-footer"); if (mainFooterElement) mainFooterElement.remove();var chapterPageElement = document.getElementById("chapter-page"); if (chapterContentElement) { chapterPageElement.style.maxWidth = "none"; } var mainElement = document.getElementById("main"); if (mainElement) { mainElement.style.marginTop = "0"; mainElement.style.marginRight = "20px"; } '
      });
    });
  });
});
