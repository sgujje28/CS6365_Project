document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append("file", file);

  // Extract Text
  const extractRes = await fetch("/extract_text/", {
    method: "POST",
    body: formData,
  });
  const extractData = await extractRes.json();
  const extractedText = extractData.extracted_text || "Error extracting text.";
  document.getElementById("extractedText").textContent = extractedText;

  // Summarize
  const summarizeRes = await fetch("/summarize_text/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: extractedText }),
  });
  const summaryData = await summarizeRes.json();
  document.getElementById("summary").textContent =
    summaryData.summary || summaryData.original_text;

  // Flashcards
  const flashRes = await fetch("/generate_flashcards/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: extractedText }),
  });
  const flashData = await flashRes.json();
  const list = document.getElementById("flashcards");
  list.innerHTML = "";
  (flashData.flashcards || []).forEach((card) => {
    const li = document.createElement("li");
    li.textContent = card;
    list.appendChild(li);
  });
});
