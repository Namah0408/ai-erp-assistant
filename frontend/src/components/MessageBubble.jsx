import { Bot, User } from "lucide-react";

function MessageBubble({ role, content }) {
  const isUser = role === "user";

  return (
    <div
      className={`flex gap-3 px-6 py-4 ${
        isUser ? "justify-end" : "justify-start"
      }`}
    >

      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-gray-900 text-white flex items-center justify-center flex-shrink-0">
          <Bot size={17} />
        </div>
      )}

      <div
        className={`max-w-2xl rounded-2xl px-4 py-3 ${
          isUser
            ? "bg-gray-900 text-white"
            : "bg-gray-100 text-gray-900"
        }`}
      >
        <p className="text-sm leading-6 whitespace-pre-wrap">
          {content}
        </p>
      </div>

      {isUser && (
        <div className="w-8 h-8 rounded-full bg-gray-200 text-gray-700 flex items-center justify-center flex-shrink-0">
          <User size={17} />
        </div>
      )}

    </div>
  );
}

export default MessageBubble;