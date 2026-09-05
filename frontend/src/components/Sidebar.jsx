import {
  MessageSquare,
  Plus,
  Settings,
} from "lucide-react";


function Sidebar({
  chats,
  activeThreadId,
  onNewChat,
  onSelectChat,
}) {
  return (
    <aside className="w-64 h-screen bg-gray-950 text-white flex flex-col flex-shrink-0">

      <div className="px-5 py-5 border-b border-gray-800">

        <div className="flex items-center gap-2">

          <div className="w-8 h-8 rounded-lg bg-white text-gray-950 flex items-center justify-center font-bold">
            ✦
          </div>

          <div className="min-w-0">

            <h1 className="font-semibold text-sm">
              ERP Assistant
            </h1>

            <p className="text-xs text-gray-400 truncate">
              Lighthouse Infosystems
            </p>

          </div>

        </div>

      </div>


      <div className="p-4">

        <button
          onClick={onNewChat}
          className="w-full flex items-center justify-center gap-2 bg-white text-gray-900 rounded-lg px-4 py-2.5 text-sm font-medium hover:bg-gray-200 transition"
        >
          <Plus size={17} />
          New Chat
        </button>

      </div>


      <div className="flex-1 overflow-y-auto px-3">

        <p className="text-xs text-gray-500 px-2 mb-2">
          Recent chats
        </p>


        {chats.length === 0 ? (

          <p className="text-xs text-gray-600 px-2 py-3">
            No conversations yet
          </p>

        ) : (

          <div className="space-y-1">

            {chats.map((chat) => (

              <button
                key={chat.threadId}
                onClick={() =>
                  onSelectChat(
                    chat.threadId
                  )
                }
                title={chat.title}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-left text-sm transition ${
                  chat.threadId ===
                  activeThreadId
                    ? "bg-gray-800 text-white"
                    : "text-gray-400 hover:bg-gray-900 hover:text-white"
                }`}
              >

                <MessageSquare
                  size={16}
                  className="flex-shrink-0"
                />

                <span className="truncate">
                  {chat.title}
                </span>

              </button>

            ))}

          </div>

        )}

      </div>


      <div className="p-3 border-t border-gray-800">

        <button
          className="w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm text-gray-400 hover:bg-gray-900 hover:text-white transition"
        >
          <Settings size={17} />
          Settings
        </button>

      </div>

    </aside>
  );
}


export default Sidebar;