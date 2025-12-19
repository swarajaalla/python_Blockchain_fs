import { useState } from "react";
import { registerUser } from "../api/auth";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
    role: "corporate", // default role
    org_name: ""
  });

  const [error, setError] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    const res = await registerUser({
      name: form.name,
      email: form.email,
      password: form.password,
      role: form.role,
      org_name: form.org_name
    });

    if (res.id) {
      navigate("/");
    } else {
      setError(res.detail || "Registration failed");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form
        onSubmit={handleRegister}
        className="bg-white shadow-lg p-8 rounded w-96 space-y-4"
      >
        <h1 className="text-2xl font-bold text-center mb-4">Register</h1>

        {error && <p className="text-red-600 text-center text-sm">{error}</p>}

        <input
          className="w-full border p-2 rounded"
          placeholder="Full Name"
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />

        <input
          className="w-full border p-2 rounded"
          placeholder="Email"
          onChange={(e) => setForm({ ...form, email: e.target.value })}
        />

        <input
          type="password"
          className="w-full border p-2 rounded"
          placeholder="Password"
          onChange={(e) => setForm({ ...form, password: e.target.value })}
        />

        {/* Role Selection */}
        <select
          className="w-full border p-2 rounded"
          value={form.role}
          onChange={(e) => setForm({ ...form, role: e.target.value })}
        >
          <option value="bank">Bank</option>
          <option value="corporate">Corporate</option>
          <option value="auditor">Auditor</option>
          <option value="admin">Admin</option>
        </select>

        {/* Organization Name */}
        <input
          className="w-full border p-2 rounded"
          placeholder="Organization Name"
          onChange={(e) => setForm({ ...form, org_name: e.target.value })}
        />

        <button className="w-full bg-green-600 text-white p-2 rounded hover:bg-green-700">
          Register
        </button>
      </form>
    </div>
  );
}
