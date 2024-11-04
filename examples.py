from reflection_agent import ReflectionAgent

if __name__ == "__main__":
    # Initialize agent
    agent = ReflectionAgent()

    # Define prompts
    generation_prompt = "You are a Python programmer tasked with generating high-quality Python code."
    reflection_prompt = "You are an experienced code reviewer. Provide detailed feedback for improving the code."
    user_msg = "Generate a Python implementation of quick sort."

    # Run reflection loop
    result = agent.run(
        user_msg=user_msg,
        generation_system_prompt=generation_prompt,
        reflection_system_prompt=reflection_prompt,
        n_steps=2,
        verbose=1
    )

    print("Final Refined Output:", result)
