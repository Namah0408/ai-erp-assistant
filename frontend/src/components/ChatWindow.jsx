import Header from "./Header";
import WelcomeScreen from "./WelcomeScreen";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

function ChatWindow() {
  const messages = [];

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
        </div>
      )}

      <ChatInput />

    </main>
  );
}

export default ChatWindow;