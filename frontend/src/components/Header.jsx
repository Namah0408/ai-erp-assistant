import { Bot } from "lucide-react";

function Header() {
  return (
    <header className="h-16 border-b border-gray-200 flex items-center px-6 bg-white">

      <div className="flex items-center gap-3">

        <div className="w-9 h-9 rounded-full bg-gray-900 text-white flex items-center justify-center">
          <Bot size={20} />
        </div>

        <div>
          <h2 className="font-semibold text-gray-900">
            AI ERP Assistant
          </h2>

          <p className="text-xs text-gray-500">
            NovaTech Industries
          </p>
        </div>

      </div>

    </header>
  );
}

export default Header;