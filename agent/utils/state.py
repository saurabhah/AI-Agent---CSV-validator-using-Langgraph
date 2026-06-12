from typing import Optional
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from typing import Annotated, TypedDict
import operator

 
class ValidationState(TypedDict, total=False):
    file_path: str
    db_table: str
    csv_rows: list[dict]         
    db_schema: dict               
    flagged: list[dict]        
    valid: list[dict]           
    human_decision: Optional[str]
    report: str
    errors: list[dict]
 

