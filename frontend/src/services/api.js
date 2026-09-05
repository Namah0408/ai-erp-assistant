const API_BASE_URL = "http://127.0.0.1:8000";


export async function sendMessage(question, threadId) {
  const response = await fetch(
    `${API_BASE_URL}/chat/`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        question: question,
        thread_id: threadId,
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      `Server error: ${response.status}`
    );
  }

  return await response.json();
}


export async function getChatHistory(threadId) {
  const response = await fetch(
    `${API_BASE_URL}/chat/history/${threadId}`
  );

  if (!response.ok) {
    throw new Error(
      `History error: ${response.status}`
    );
  }

  return await response.json();
}