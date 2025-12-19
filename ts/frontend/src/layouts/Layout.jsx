import React, { useContext } from "react";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import { AuthContext } from "../context/AuthContext";

export default function Layout({ children }) {
  const { user } = useContext(AuthContext);
  const role = user?.role || "corporate";

  return (
    <div className="flex">
      <Sidebar role={role} />
      <div className="flex-1 min-h-screen bg-gray-50">
        <Navbar />
        <main className="p-6">{children}</main>
      </div>
    </div>
  );
}
