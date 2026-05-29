from typing import Optional
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from typing import Annotated, TypedDict
import operator

 
class ValidationState(TypedDict, total=False):
    file_path: str
    db_table: str
    csv_rows: list[dict]          # raw rows from file
    db_schema: dict               # schema fetched from postgres
    flagged: list[dict]           # rows flagged by the agent with reasons
    valid: list[dict]             # rows that passed
    human_decision: Optional[str] # accept / reject per flagged row
    report: str
    errors: list[dict]
 

