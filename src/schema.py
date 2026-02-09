from pydantic import BaseModel, Field
from typing import List, Literal, Dict, Any, Union

class NetworkAction(BaseModel):
    component: Literal['bus', 'line', 'load', 'gen', 'sgen'] = Field(
        description="The type of grid component to modify."
    )
    id: int = Field(
        description="The integer ID/index of the component."
    )
    type: Literal['modify', 'create'] = Field(
        description="The type of action to perform. Use 'modify' for existing components."
    )
    parameters: Dict[str, Any] = Field(
        description="Key-value pairs of parameters to set (e.g., {'p_mw': 50.0, 'in_service': False}). Values must be primitives."
    )

class ScenarioResponse(BaseModel):
    actions: List[NetworkAction] = Field(
        description="List of actions to apply to the network to fulfill the user request."
    )
