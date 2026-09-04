import { useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";

function ChatPage() {

  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  return (
    <div className="flex h-screen overflow-hidden">

      <Sidebar />

      <ChatWindow
        messages={messages}
        setMessages={setMessages}
        loading={loading}
        setLoading={setLoading}
      />

    </div>
  );
}

export default ChatPage;