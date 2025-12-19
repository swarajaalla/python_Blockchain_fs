import React from "react";

export default function Dashboard() {
  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-semibold">Dashboard Overview</h2>

      <div className="grid grid-cols-3 gap-4">
        <div className="p-4 bg-white rounded shadow">Total Documents: <strong>128</strong></div>
        <div className="p-4 bg-white rounded shadow">Active Trades: <strong>23</strong></div>
        <div className="p-4 bg-white rounded shadow">Disputes: <strong>2</strong></div>
      </div>

      <div className="mt-6 bg-white p-4 rounded shadow">
        <h3 className="font-semibold">Recent Activity</h3>
        <ul className="mt-2 text-sm text-gray-600">
          <li>Invoice INV-1001 issued by Acme Corp</li>
          <li>Bill of Lading BOL-200 verified</li>
          <li>Risk score updated for Counterparty XYZ</li>
        </ul>
      </div>
    </div>
  );
}
