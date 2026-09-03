import {
  Plus,
  MessageSquare,
  Settings,
  PanelLeftClose,
} from "lucide-react";

function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-gray-900 text-white flex flex-col">

      {/* Logo */}
      <div className="p-4 border-b border-gray-700">
        <h1 className="text-lg font-semibold">
          ✦ ERP Assistant
        </h1>
        <p className="text-xs text-gray-400 mt-1">
          NovaTech Industries
        </p>
      </div>

      {/* New Chat */}
      <div className="p-3">
        <button className="w-full flex items-center gap-2 px-4 py-3 rounded-lg border border-gray-700 hover:bg-gray-800 transition">
          <Plus size={18} />
          <span>New Chat</span>
        </button>
      </div>

      {/* Recent Chats */}
      <div className="flex-1 overflow-y-auto px-3">

        <p className="text-xs text-gray-500 px-2 py-2">
          RECENT
        </p>

        <button className="w-full flex items-center gap-3 px-3 py-3 rounded-lg hover:bg-gray-800 text-sm text-left">
          <MessageSquare size={16} />
          <span>Inventory Query</span>
        </button>

        <button className="w-full flex items-center gap-3 px-3 py-3 rounded-lg hover:bg-gray-800 text-sm text-left">
          <MessageSquare size={16} />
          <span>Leave Policy</span>
        </button>

        <button className="w-full flex items-center gap-3 px-3 py-3 rounded-lg hover:bg-gray-800 text-sm text-left">
          <MessageSquare size={16} />
          <span>Invoice Status</span>
        </button>

      </div>

      {/* Bottom */}
      <div className="p-3 border-t border-gray-700">

        <button className="w-full flex items-center gap-3 px-3 py-3 rounded-lg hover:bg-gray-800 text-sm">
          <Settings size={18} />
          <span>Settings</span>
        </button>

      </div>

    </aside>
  );
}

export default Sidebar;