from src.agents.orchestrator import Orchestrator
import sys

def main():
    print("--- Geo-Spatial Power Grid Agent System ---")
    
    # 1. Initialize
    try:
        orch = Orchestrator(network_name="case57", n_clusters=3) # Use 3 regions for Case 57
    except Exception as e:
        print(f"Initialization Failed: {e}")
        return

    # 2. Check for Single Shot CLI Args
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        process_query(orch, query)
        return

    # 3. Interactive Loop
    print("\nSystem Ready. Enter commands (e.g., 'Outage bus 2', 'Status') or 'exit' to quit.")
    
    while True:
        try:
            user_input = input("\n>> ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit", "q"]:
                print("Exiting...")
                break
            
            process_query(orch, user_input)
            
        except KeyboardInterrupt:
            print("\nUser interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def process_query(orch, query):
    # Simple intent detection (can be improved with LLM router later)
    # If the user asks to "outage", "modify", "increase", "create case", etc., we use the scenario modifier.
    modification_keywords = ["outage", "modify", "increase", "decrease", "set", "create case", "disconnect", "change"]
    
    if any(k in query.lower() for k in modification_keywords):
        response = orch.process_scenario_modification(query)
    else:
        response = orch.process_user_query(query)
    
    print("\n================ RESPONSE ================")
    print(response)
    print("==========================================")

if __name__ == "__main__":
    main()
