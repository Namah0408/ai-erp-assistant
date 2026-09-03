import { Send } from "lucide-react";

function ChatInput() {
  return (
    <div className="border-t border-gray-200 p-4 bg-white">

      <div className="max-w-4xl mx-auto">

        <div className="flex items-center gap-3 border border-gray-300 rounded-2xl px-4 py-2 focus-within:ring-2 focus-within:ring-gray-200">

          <input
            type="text"
            placeholder="Ask anything about NovaTech..."
            className="flex-1 outline-none text-sm bg-transparent"
          />

          <button
            className="w-9 h-9 rounded-xl bg-gray-900 text-white flex items-center justify-center hover:bg-gray-700 transition"
          >
            <Send size={17} />
          </button>

        </div>

        <p className="text-xs text-gray-400 text-center mt-2">
          AI ERP Assistant can make mistakes. Verify important information.
        </p>

      </div>

    </div>
  );
}

export default ChatInput;