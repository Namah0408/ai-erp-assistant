import { useState } from "react";
import { Send } from "lucide-react";

import { sendMessage } from "../services/api";

function ChatInput({
  messages,
  setMessages,
  loading,
  setLoading
}) {
  const [input, setInput] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();

    const question = input.trim();

    if (!question || loading) {
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
      const data = await sendMessage(
        question,
        "default-thread"
      );

      // Extract plain text from the AI response
      let answer = data.answer;

      if (Array.isArray(answer)) {
        answer = answer
          .map((item) => {
            if (typeof item === "string") {
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

      if (typeof answer !== "string") {
        answer = String(answer);
      }

      const aiMessage = {
        role: "ai",
        content: answer,
      };

      setMessages((prev) => [
        ...prev,
        aiMessage,
      ]);

    } catch (error) {
      console.error("Chat error:", error);

      const errorMessage = {
        role: "ai",
        content:
          "Sorry, something went wrong while communicating with the server.",
      };

      setMessages((prev) => [
        ...prev,
        errorMessage,
      ]);

    } finally {
      setLoading(false);
    }
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
              setInput(event.target.value)
            }
            placeholder="Ask anything about Lighthouse..."
            disabled={loading}
            className="flex-1 outline-none text-sm bg-transparent"
          />

          <button
            type="submit"
            disabled={loading || !input.trim()}
            className="w-9 h-9 rounded-xl bg-gray-900 text-white flex items-center justify-center hover:bg-gray-700 transition disabled:opacity-40"
          >
            <Send size={17} />
          </button>

        </div>

        <p className="text-xs text-gray-400 text-center mt-2">
          AI ERP Assistant can make mistakes. Verify important information.
        </p>
      </form>
    </div>
  );
}

export default ChatInput;