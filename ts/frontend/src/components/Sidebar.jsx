import React from "react";
import { Link, useLocation } from "react-router-dom";

/**
 * role: 'bank' | 'corporate' | 'auditor' | 'admin'
 */
export default function Sidebar({ role }) {
  const loc = useLocation();
  const items = [
    { key: "dashboard", label: "Overview", path: "/dashboard", roles: ["bank","corporate","auditor","admin"] },
    { key: "documents", label: "Documents", path: "/documents", roles: ["bank","corporate","admin"] },
    { key: "ledger", label: "Ledger Explorer", path: "/ledger", roles: ["bank","corporate","auditor","admin"] },
    { key: "risk", label: "Risk Scores", path: "/risk", roles: ["bank","admin"] },
    { key: "audit", label: "Audit Logs", path: "/audit", roles: ["admin","auditor"] }
  ];

  return (
    <div className="w-64 bg-gray-800 text-white min-h-screen p-4">
      <div className="mb-6">
        <div className="text-lg font-bold">Menu</div>
      </div>

      <nav className="flex flex-col gap-2">
        {items.map(item => {
          if (!item.roles.includes(role)) return null;
          const active = loc.pathname === item.path;
          return (
            <Link
              key={item.key}
              to={item.path}
              className={`block px-3 py-2 rounded ${active ? "bg-gray-700" : "hover:bg-gray-700"}`}
            >
              {item.label}
            </Link>
          );
        })}
      </nav>
    </div>
  );
}
