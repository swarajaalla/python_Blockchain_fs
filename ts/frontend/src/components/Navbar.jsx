import React, { useContext } from "react";
import { AuthContext } from "../context/AuthContext";

export default function Navbar() {
  const { user, logout } = useContext(AuthContext);

  return (
    <div className="flex items-center justify-between bg-white px-6 py-3 shadow">
      <div className="flex items-center gap-4">
        <h1 className="text-xl font-bold">ChainDocs</h1>
        <span className="text-sm text-gray-500">Trade Finance Explorer</span>
      </div>

      <div className="flex items-center gap-4">
        {user && (
          <>
            <div className="text-right">
              <div className="text-sm font-semibold">{user.name || user.email}</div>
              <div className="text-xs text-gray-500">{user.role}</div>
            </div>
            <button
              onClick={logout}
              className="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded"
            >
              Logout
            </button>
          </>
        )}
      </div>
    </div>
  );
}
