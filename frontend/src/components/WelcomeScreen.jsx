function WelcomeScreen({
  onSuggestionClick,
}) {
  const suggestions = [
    {
      title: "Check inventory",
      question:
        "Show me the products that are low in stock.",
    },
    {
      title: "Check invoices",
      question:
        "Show me our unpaid invoices.",
    },
    {
      title: "Employee information",
      question:
        "Show me the employees in the HR department.",
    },
    {
      title: "Company policies",
      question:
        "How many casual leaves are NovaTech employees allowed?",
    },
  ];


  return (
    <div className="flex-1 overflow-y-auto flex flex-col items-center justify-center px-4 sm:px-6">

      <div className="text-center max-w-2xl">

        <div className="w-14 h-14 rounded-2xl bg-gray-900 text-white flex items-center justify-center text-2xl mx-auto mb-5">
          ✦
        </div>


        <h2 className="text-2xl sm:text-3xl font-semibold text-gray-900">
          How can I help you?
        </h2>


        <p className="text-gray-500 mt-2 text-sm sm:text-base">
          Ask me about employees, inventory,
          invoices, procurement, or company policies.
        </p>

      </div>


      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 max-w-2xl w-full mt-8">

        {suggestions.map(
          (suggestion) => (

            <button
              key={suggestion.title}
              onClick={() =>
                onSuggestionClick(
                  suggestion.question
                )
              }
              className="text-left border border-gray-200 rounded-xl p-4 hover:border-gray-400 hover:bg-gray-50 transition"
            >

              <p className="text-sm font-medium text-gray-900">
                {suggestion.title}
              </p>

              <p className="text-xs text-gray-500 mt-1 leading-5">
                {suggestion.question}
              </p>

            </button>

          )
        )}

      </div>

    </div>
  );
}


export default WelcomeScreen;