import { useEffect, useRef } from "react";

import Header from "./Header";
import WelcomeScreen from "./WelcomeScreen";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";


function ChatWindow({
  messages,
  setMessages,
  loading,
  setLoading,
  threadId,
  onConversationCreated,
}) {
  const messagesEndRef =
    useRef(null);


  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);


  return (
    <main className="flex-1 h-screen min-w-0 flex flex-col bg-white">

      <Header />


      {messages.length === 0 ? (

        <WelcomeScreen
          onSuggestionClick={(question) => {
            const event =
              new CustomEvent(
                "erp-suggestion",
                {
                  detail: question,
                }
              );

            window.dispatchEvent(event);
          }}
        />

      ) : (

        <div className="flex-1 overflow-y-auto">

          <div className="max-w-5xl mx-auto">

            {messages.map(
              (message, index) => (
                <MessageBubble
                  key={`${threadId}-${index}`}
                  role={message.role}
                  content={message.content}
                />
              )
            )}


            {loading && (

              <div className="px-4 sm:px-6 py-4">

                <div className="flex items-center gap-3">

                  <div className="w-8 h-8 rounded-full bg-gray-900 text-white flex items-center justify-center flex-shrink-0">
                    ✦
                  </div>

                  <div className="bg-gray-100 rounded-2xl px-4 py-3">

                    <div className="flex gap-1">

                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" />

                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.15s]" />

                      <span className="w-2 h-2 bg-gray-400 rounded-full animate-bounce [animation-delay:0.3s]" />

                    </div>

                  </div>

                </div>

              </div>

            )}

            <div ref={messagesEndRef} />

          </div>

        </div>

      )}


      <ChatInput
        messages={messages}
        setMessages={setMessages}
        loading={loading}
        setLoading={setLoading}
        threadId={threadId}
        onConversationCreated={
          onConversationCreated
        }
      />

    </main>
  );
}


export default ChatWindow;