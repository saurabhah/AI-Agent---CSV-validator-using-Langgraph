from langgraph.graph import StateGraph,START, END
from utils.state import ValidationState
from utils.nodes import load_csv_node, schema_node, validation_node
from utils.db_connection import get_schema
from dotenv import load_dotenv

load_dotenv()

def main():
    workflow = StateGraph(ValidationState)
    print("Running Workflow")
    workflow.add_node("load_csv", load_csv_node)
    workflow.add_node("schema", schema_node)
    workflow.add_node("validate", validation_node)

    workflow.set_entry_point("load_csv")

    workflow.add_edge("load_csv", "schema")
    workflow.add_edge("schema", "validate")
    workflow.add_edge("validate", END)

    graph = workflow.compile()

    print("Invoke Graph")


    result = graph.invoke({
            "file_path": "data/employee_insert.csv",
            "db_table": "employees_details",
        })

    return result


if __name__ == "__main__":
    result = main()
    # print("Validation Result:")
    # print(result)