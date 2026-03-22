from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

class ArithmeticInput(BaseModel):
    num1: float = Field(..., description="The first number")
    num2: float = Field(..., description="The second number")

class ArithmeticOutput(BaseModel):
    result: float = Field(..., description="The result of the arithmetic operation")    
    expression: str = Field(..., description="Expression Evaluated")

mcp = FastMCP(
    "arithmetic_server",
    host="localhost",
    port=3000,
    stateless_http=True
    )

@mcp.tool("add_numbers")
async def add_numbers(input: ArithmeticInput) -> ArithmeticOutput:
    """
    Add two numbers and return the result along with the expression evaluated.
    Args:
        input (ArithmeticInput): An object containing two numbers to be added.
    Returns:
        ArithmeticOutput: An object containing the result of the addition and the expression evaluated.
    """
    result = input.num1 + input.num2
    expression = f"{input.num1} + {input.num2} = {result}"
    return ArithmeticOutput(result=result, expression=expression)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")   