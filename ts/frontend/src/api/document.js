import axios from "axios";

export const uploadDocument = async (formData, token) => {
  return axios.post(
    "http://localhost:8000/documents/upload",
    formData,
    {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "multipart/form-data",
      },
    }
  );
};
