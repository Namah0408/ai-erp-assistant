import {
  useEffect,
  useState,
} from "react";

import { Send } from "lucide-react";

import { sendMessage } from "../services/api";


function ChatInput({
  messages,
  setMessages,
  loading,
  setLoading,
  threadId,
  onConversationCreated,
}) {
  const [input, setInput] =
    useState("");


  useEffect(() => {
    function handleSuggestion(event) {
      const question =
        event.detail;

      if (!question || loading) {
        return;
      }

      setInput(question);

      setTimeout(() => {
        submitQuestion(question);
      }, 50);
    }

    window.addEventListener(
      "erp-suggestion",
      handleSuggestion
    );

    return () => {
      window.removeEventListener(
        "erp-suggestion",
        handleSuggestion
      );
    };
  }, [loading, threadId]);


  function extractAnswer(answer) {
    if (typeof answer === "string") {
      return answer;
    }


    if (Array.isArray(answer)) {
      return answer
        .map((item) => {

          if (
            typeof item ===
            "string"
          ) {
            return item;
          }

          if (item?.text) {
            return item.text;
          }

          return "";

        })
        .filter(Boolean)
        .join("\n");
    }


    if (answer?.text) {
      return answer.text;
    }


    return String(
      answer || ""
    );
  }


  async function submitQuestion(
    question
  ) {
    if (
      !question ||
      loading ||
      !threadId
    ) {
      return;
    }


    const userMessage = {
      role: "user",
      content: question,
    };


    setMessages((prev) => [
      ...prev,
      userMessage,
    ]);

    setInput("");
    setLoading(true);


    try {

      const data =
        await sendMessage(
          question,
          threadId
        );


      const answer =
        extractAnswer(
          data.answer
        );


      const aiMessage = {
        role: "ai",
        content:
          answer ||
          "I couldn't generate a response.",
      };


      setMessages((prev) => [
        ...prev,
        aiMessage,
      ]);


      onConversationCreated(
        question,
        threadId
      );


    } catch (error) {

      console.error(
        "Chat error:",
        error
      );


      let errorText =
        "Sorry, I couldn't process your request.";

      if (
        error.message?.includes(
          "Failed to fetch"
        )
      ) {
        errorText =
          "Unable to connect to the ERP server. Please make sure the backend is running.";
      }


      const errorMessage = {
        role: "ai",
        content: errorText,
      };


      setMessages((prev) => [
        ...prev,
        errorMessage,
      ]);

    } finally {

      setLoading(false);

    }
  }


  async function handleSubmit(
    event
  ) {
    event.preventDefault();

    const question =
      input.trim();

    await submitQuestion(
      question
    );
  }


  return (
    <div className="border-t border-gray-200 p-4 bg-white">

      <form
        onSubmit={handleSubmit}
        className="max-w-4xl mx-auto"
      >

        <div className="flex items-center gap-3 border border-gray-300 rounded-2xl px-4 py-2 focus-within:ring-2 focus-within:ring-gray-200">

          <input
            type="text"
            value={input}
            onChange={(event) =>
              setInput(
                event.target.value
              )
            }
            placeholder="Ask anything about Lighthouse..."
            disabled={loading}
            className="flex-1 outline-none text-sm bg-transparent min-w-0"
          />


          <button
            type="submit"
            disabled={
              loading ||
              !input.trim()
            }
            className="w-9 h-9 rounded-xl bg-gray-900 text-white flex items-center justify-center hover:bg-gray-700 transition disabled:opacity-40 flex-shrink-0"
          >
            <Send size={17} />
          </button>

        </div>


        <p className="text-xs text-gray-400 text-center mt-2">
          AI ERP Assistant can make mistakes.
          Verify important information.
        </p>

      </form>

    </div>
  );
}


export default ChatInput;