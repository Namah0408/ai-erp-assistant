import {
  Package,
  FileText,
  Users,
  ClipboardList,
} from "lucide-react";

function WelcomeScreen() {
  return (
    <div className="flex-1 flex flex-col items-center justify-center px-6">

      <div className="w-16 h-16 rounded-2xl bg-gray-900 text-white flex items-center justify-center mb-6">
        <span className="text-2xl">✦</span>
      </div>

      <h1 className="text-3xl font-semibold text-gray-900">
        How can I help you?
      </h1>

      <p className="text-gray-500 mt-2 text-center max-w-md">
        Ask about employees, inventory, invoices,
        purchase orders, or company policies.
      </p>

      <div className="grid grid-cols-2 gap-3 mt-8 max-w-lg w-full">

        <button className="border border-gray-200 rounded-xl p-4 text-left hover:bg-gray-50 transition">
          <Package size={20} />
          <p className="font-medium mt-2">
            Check inventory
          </p>
          <p className="text-xs text-gray-500 mt-1">
            Find stock levels and products
          </p>
        </button>

        <button className="border border-gray-200 rounded-xl p-4 text-left hover:bg-gray-50 transition">
          <FileText size={20} />
          <p className="font-medium mt-2">
            Check invoices
          </p>
          <p className="text-xs text-gray-500 mt-1">
            Find unpaid or overdue invoices
          </p>
        </button>

        <button className="border border-gray-200 rounded-xl p-4 text-left hover:bg-gray-50 transition">
          <Users size={20} />
          <p className="font-medium mt-2">
            Employee information
          </p>
          <p className="text-xs text-gray-500 mt-1">
            Search employee details
          </p>
        </button>

        <button className="border border-gray-200 rounded-xl p-4 text-left hover:bg-gray-50 transition">
          <ClipboardList size={20} />
          <p className="font-medium mt-2">
            Company policies
          </p>
          <p className="text-xs text-gray-500 mt-1">
            Ask about internal policies
          </p>
        </button>

      </div>

    </div>
  );
}

export default WelcomeScreen;