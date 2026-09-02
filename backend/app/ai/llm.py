from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.tools.employee_tools import (
    search_employees,
    get_employee_details,
    get_employee_leaves
)

from app.tools.inventory_tools import (
    search_products,
    get_low_stock_products,
    get_product_stock
)

from app.tools.invoice_tools import (
    search_invoices,
    get_unpaid_invoices,
    get_overdue_invoices
)

from app.tools.procurement_tools import (
    get_pending_purchase_orders,
    search_purchase_orders,
    create_purchase_order
)


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


tools = [
    search_employees,
    get_employee_details,
    get_employee_leaves,

    search_products,
    get_low_stock_products,
    get_product_stock,

    search_invoices,
    get_unpaid_invoices,
    get_overdue_invoices,

    get_pending_purchase_orders,
    search_purchase_orders,
    create_purchase_order
]


llm_with_tools = llm.bind_tools(tools)