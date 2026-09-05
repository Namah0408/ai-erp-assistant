import { Bot, User, Copy, Check } from "lucide-react";
import ReactMarkdown from "react-markdown";
import { useState } from "react";


function MessageBubble({ role, content }) {
  const isUser = role === "user";

  const [copied, setCopied] =
    useState(false);


  async function handleCopy() {
    try {
      await navigator.clipboard.writeText(
        content
      );

      setCopied(true);

      setTimeout(() => {
        setCopied(false);
      }, 1500);

    } catch (error) {
      console.error(
        "Copy failed:",
        error
      );
    }
  }


  return (
    <div
      className={`flex gap-3 px-4 sm:px-6 py-4 ${
        isUser
          ? "justify-end"
          : "justify-start"
      }`}
    >

      {!isUser && (
        <div className="w-8 h-8 rounded-full bg-gray-900 text-white flex items-center justify-center flex-shrink-0">
          <Bot size={17} />
        </div>
      )}


      <div
        className={`max-w-3xl rounded-2xl px-4 py-3 ${
          isUser
            ? "bg-gray-900 text-white"
            : "bg-gray-100 text-gray-900"
        }`}
      >

        <div className="text-sm leading-6 break-words">

          {isUser ? (

            <p className="whitespace-pre-wrap">
              {content}
            </p>

          ) : (

            <ReactMarkdown
              components={{
                p: ({ children }) => (
                  <p className="mb-3 last:mb-0">
                    {children}
                  </p>
                ),

                ul: ({ children }) => (
                  <ul className="list-disc ml-5 mb-3 space-y-1">
                    {children}
                  </ul>
                ),

                ol: ({ children }) => (
                  <ol className="list-decimal ml-5 mb-3 space-y-1">
                    {children}
                  </ol>
                ),

                strong: ({ children }) => (
                  <strong className="font-semibold">
                    {children}
                  </strong>
                ),

                h1: ({ children }) => (
                  <h1 className="text-lg font-semibold mb-2">
                    {children}
                  </h1>
                ),

                h2: ({ children }) => (
                  <h2 className="text-base font-semibold mb-2">
                    {children}
                  </h2>
                ),

                h3: ({ children }) => (
                  <h3 className="font-semibold mb-2">
                    {children}
                  </h3>
                ),

                code: ({ children }) => (
                  <code className="bg-gray-200 px-1.5 py-0.5 rounded text-xs">
                    {children}
                  </code>
                ),

                table: ({ children }) => (
                  <div className="overflow-x-auto mb-3">
                    <table className="min-w-full border-collapse text-sm">
                      {children}
                    </table>
                  </div>
                ),

                th: ({ children }) => (
                  <th className="border border-gray-300 px-3 py-2 text-left font-semibold">
                    {children}
                  </th>
                ),

                td: ({ children }) => (
                  <td className="border border-gray-300 px-3 py-2">
                    {children}
                  </td>
                ),
              }}
            >
              {content}
            </ReactMarkdown>

          )}

        </div>


        {/* Copy button for AI responses */}

        {!isUser && (
          <div className="flex justify-end mt-2">

            <button
              onClick={handleCopy}
              className="flex items-center gap-1 text-xs text-gray-500 hover:text-gray-900 transition"
              title="Copy response"
            >

              {copied ? (
                <>
                  <Check size={13} />
                  Copied
                </>
              ) : (
                <>
                  <Copy size={13} />
                  Copy
                </>
              )}

            </button>

          </div>
        )}

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