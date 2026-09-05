import { useEffect, useState } from "react";

import Sidebar from "../components/Sidebar";
import ChatWindow from "../components/ChatWindow";
import { getChatHistory } from "../services/api";


function generateThreadId() {
  if (crypto.randomUUID) {
    return crypto.randomUUID();
  }

  return `thread-${Date.now()}`;
}


function getStoredChats() {
  try {
    const storedChats =
      localStorage.getItem(
        "erp_chats"
      );

    return storedChats
      ? JSON.parse(storedChats)
      : [];

  } catch {
    return [];
  }
}


function ChatPage() {
  const [chats, setChats] =
    useState(getStoredChats);

  const [activeThreadId, setActiveThreadId] =
    useState(() => {
      return localStorage.getItem(
        "active_thread_id"
      );
    });

  const [messages, setMessages] =
    useState([]);

  const [loading, setLoading] =
    useState(false);


  useEffect(() => {
    localStorage.setItem(
      "erp_chats",
      JSON.stringify(chats)
    );
  }, [chats]);


  useEffect(() => {
    if (activeThreadId) {
      localStorage.setItem(
        "active_thread_id",
        activeThreadId
      );
    }
  }, [activeThreadId]);


  useEffect(() => {
    if (
      !activeThreadId &&
      chats.length === 0
    ) {
      setActiveThreadId(
        generateThreadId()
      );
    }
  }, [
    activeThreadId,
    chats.length,
  ]);


  useEffect(() => {
    async function loadHistory() {

      if (!activeThreadId) {
        return;
      }


      try {

        setLoading(true);

        const data =
          await getChatHistory(
            activeThreadId
          );


        const history =
          data.messages ||
          data.history ||
          [];


        const formattedMessages =
          history
            .map((message) => {

              let content =
                message.content;


              if (
                Array.isArray(content)
              ) {
                content =
                  content
                    .map((item) =>
                      typeof item ===
                      "string"
                        ? item
                        : item?.text || ""
                    )
                    .filter(Boolean)
                    .join("\n");
              }


              return {
                role:
                  message.role ===
                  "human"
                    ? "user"
                    : message.role ===
                      "ai"
                    ? "ai"
                    : message.role,

                content:
                  typeof content ===
                  "string"
                    ? content
                    : String(
                        content || ""
                      ),
              };

            })
            .filter(
              (message) =>
                message.content
            );


        setMessages(
          formattedMessages
        );

      } catch (error) {

        console.error(
          "Failed to load chat history:",
          error
        );

        setMessages([]);

      } finally {

        setLoading(false);

      }
    }


    loadHistory();

  }, [activeThreadId]);


  function handleNewChat() {

    const newThreadId =
      generateThreadId();


    setActiveThreadId(
      newThreadId
    );

    setMessages([]);

    setLoading(false);
  }


  function handleSelectChat(
    threadId
  ) {

    if (
      threadId ===
      activeThreadId
    ) {
      return;
    }


    setActiveThreadId(
      threadId
    );

    setMessages([]);
  }


  function handleConversationCreated(
    question,
    threadId
  ) {

    const existingChat =
      chats.find(
        (chat) =>
          chat.threadId ===
          threadId
      );


    if (existingChat) {
      return;
    }


    const newChat = {
      threadId,
      title:
        question.length > 40
          ? question.substring(
              0,
              40
            ) + "..."
          : question,
      createdAt:
        new Date().toISOString(),
    };


    setChats((prev) => [
      newChat,
      ...prev,
    ]);
  }


  return (
    <div className="flex h-screen overflow-hidden">

      <Sidebar
        chats={chats}
        activeThreadId={
          activeThreadId
        }
        onNewChat={
          handleNewChat
        }
        onSelectChat={
          handleSelectChat
        }
      />


      <ChatWindow
        messages={messages}
        setMessages={
          setMessages
        }
        loading={loading}
        setLoading={
          setLoading
        }
        threadId={
          activeThreadId
        }
        onConversationCreated={
          handleConversationCreated
        }
      />

    </div>
  );
}


export default ChatPage;