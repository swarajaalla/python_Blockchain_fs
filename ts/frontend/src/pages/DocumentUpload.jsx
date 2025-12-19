import { useState } from "react";
import { uploadDocument } from "../api/documents";
import { getToken } from "../utils/auth";

export default function DocumentUpload() {
  const [file, setFile] = useState(null);
  const [docType, setDocType] = useState("INVOICE");
  const [docNumber, setDocNumber] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("file", file);
    formData.append("doc_type", docType);
    formData.append("doc_number", docNumber);
    formData.append("issued_at", new Date().toISOString());

    await uploadDocument(formData, getToken());
    alert("Document uploaded!");
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <input
        placeholder="Document Number"
        onChange={(e) => setDocNumber(e.target.value)}
      />
      <select onChange={(e) => setDocType(e.target.value)}>
        <option value="INVOICE">Invoice</option>
        <option value="LOC">LoC</option>
      </select>
      <button className="bg-blue-600 text-white px-4 py-2">
        Upload
      </button>
    </form>
  );
}
