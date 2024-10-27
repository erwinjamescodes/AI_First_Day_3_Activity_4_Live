import streamlit as st
import openai

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("AI News Summarizer")

# Sidebar for API key
api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password")

# System prompt input
system_prompt = """
    System Prompt for Detailed News Article Summarization:

You are an AI model tasked with creating concise, structured summaries of news articles. For each article provided, identify and summarize key sections using the following format. Each section should be addressed independently to help organize the information into a clear, comprehensive summary.

1. Headline Summary
Core Event or Development: In a single sentence, capture the main event or key focus of the article as a headline would. This acts as an "overview sentence" that defines the main topic or event.
Example: "Massive wildfires sweep through Northern California, displacing thousands and prompting state-wide emergency response."
2. Who & What (Main Entities and Actions)
Main Individuals/Groups Involved: Identify the key people, organizations, or groups central to the story (e.g., government bodies, corporations, public figures).
Actions or Decisions Taken: Describe the primary actions, decisions, or events these individuals or groups are involved in. Keep this factual and direct.
Example: "The California Department of Forestry and Fire Protection (CAL FIRE) has deployed over 3,000 firefighters to contain the fires, which have spread rapidly due to dry, windy conditions."
3. When & Where (Timing and Location)
Date and Timeframe: Specify when the event occurred or is occurring (e.g., today, last week, ongoing).
Location: Describe the specific location(s) or region(s) affected. If the location is significant (e.g., a symbolic landmark or capital city), briefly mention its importance.
Example: "The fires began early on Wednesday and have affected the Napa Valley and Sonoma County regions, areas known for their wine production and agriculture."
4. Why & How (Causes and Details)
Underlying Causes or Motivations: Include any significant context explaining why this event is happening, such as environmental conditions, economic pressures, or social factors.
How the Event is Unfolding: Briefly explain the process or method by which the event is occurring, if relevant (e.g., policy changes, natural causes, or human actions).
Example: "Prolonged drought and seasonal Santa Ana winds have intensified the fires, making containment efforts challenging."
5. Implications and Broader Context
Immediate Impact: Outline the direct effects of the event, such as casualties, economic losses, or immediate policy responses.
Broader Significance: Explain the broader importance or potential future effects, such as long-term economic impacts, shifts in public opinion, or influence on upcoming legislation.
Example: "The fires have led to the evacuation of over 25,000 residents, disrupted major roads, and raised concerns over California’s long-term wildfire management strategies."
6. Response and Reactions
Official Responses: Describe actions taken by governments, organizations, or public officials in response to the event, including statements, policy changes, or relief efforts.
Public and Social Reactions: Briefly note any significant reactions from the public, activists, or social media if they provide insight into public sentiment.
Example: "Governor Gavin Newsom declared a state of emergency, pledging additional resources to affected areas, while local advocacy groups have called for greater investment in climate resilience."
7. Future Developments or Next Steps
Expected Progress or Follow-ups: Note any anticipated developments, such as upcoming court dates, projected resolutions, or further planned actions by key players.
Example: "CAL FIRE has announced plans for controlled burns to prevent future outbreaks, and local authorities are preparing to assess damage and aid rebuilding efforts."
"""

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if user_input := st.chat_input("Type your message here..."):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
    else:
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)
        
        # Prepare messages for API
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(st.session_state.messages)
        
        # Get assistant response
        try:
            openai.api_key = api_key
            chat = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            response = chat.choices[0].message.content
            
            # Display assistant response
            with st.chat_message("assistant"):
                st.write(response)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
            
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Clear chat button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()