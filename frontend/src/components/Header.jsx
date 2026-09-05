function Header() {
  return (
    <header className="h-16 border-b border-gray-200 flex items-center px-4 sm:px-6 flex-shrink-0 bg-white">

      <div className="flex-1">

        <h2 className="text-sm font-semibold text-gray-900">
          AI ERP Assistant
        </h2>

        <p className="text-xs text-gray-500 hidden sm:block">
          Ask questions about Lighthouse Infosystems
        </p>

      </div>

      <div className="text-xs text-gray-400">
        AI Assistant
      </div>

    </header>
  );
}


export default Header;