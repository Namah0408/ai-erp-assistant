import { useEffect, useRef } from "react";

import Header from "./Header";
import WelcomeScreen from "./WelcomeScreen";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

function ChatWindow({
  messages,
  setMessages,
  loading,
  setLoading
}) {

  const messagesEndRef = useRef(null);

  useEffect(() => {

    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth"
    });

  }, [messages, loading]);

  return (
    <main className="flex-1 h-screen flex flex-col bg-white">

      <Header />

      {messages.length === 0 ? (

        <WelcomeScreen />

      ) : (

        <div className="flex-1 overflow-y-auto">

          {messages.map((message, index) => (

            <MessageBubble
              key={index}
              role={message.role}
              content={message.content}
            />

          ))}

          {loading && (
            <div className="px-6 py-4 text-sm text-gray-500">
              AI is thinking...
            </div>
          )}

          <div ref={messagesEndRef} />

        </div>

      )}

      <ChatInput
        messages={messages}
        setMessages={setMessages}
        loading={loading}
        setLoading={setLoading}
      />

    </main>
  );
}

export default ChatWindow;