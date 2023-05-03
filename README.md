# Repository for Labs
## CMPSC 441 and GAME 450


Abstract:

The game is developed using the Python and Pygame libraries, which provide essential functionalities for the game's development. Although players have the option to move manually, they can leverage the Artificial Intelligence agent to control their movements and that of their opponents during combat. The game map is generated randomly, and it includes cities and routes between them, providing a unique experience each time a player engages the game.

The player's primary objective is to navigate through the path from start to finish without losing all their health while engaging in combat with robbers. The player has limited health, and each battle presents a chance to decrement health points. Additionally, the player can select their weapons, while the robber's weapon choice will be randomly generated.

The game's main interface is created using Pygame, while the routes and cities are randomly generated, offering an exciting challenge each time. The Artificial Intelligence agent is designed to enhance the game's difficulty by introducing unpredictability to the robber's choices, thereby making the game more engaging.

This virtual program enables users to leverage Artificial Intelligence while enjoying a turn-based gaming experience. There are specific constraints that players must adhere to while playing. For instance, the Artificial Intelligence agent is restricted from moving from one route to another if no path exists. Moreover, it can display the travel cost based on terrain, thereby creating additional challenges to win the game. The route cost and paths are randomly generated to provide a unique experience, while cities are strategically placed to adhere to rules based on terrain, water bodies, or the presence of other cities. The game features error handling exceptions, making it challenging to break.


List of AI Components: 

1. AI Player Combat
2. AI Player Movement
3. AI Journal Entry Generation


Problem Solved: 

AI Player Combat offers the ability to create an intelligent agent that can engage in combat with a player manually playing. The objective of the AI Player Combat is to take advantage of various combat strategies the game has to offer to fight off the user playing the game. Based on rule systems that are implemented, the combat agent will decide on a strategy based on its state in the game. The system takes advantage of Reinforcement Learning that enables the intelligent agent to learn from its previous decisions and change up their decision based on their health status after a few battles. 

AI Player Movement models a user interacting with the game as it takes user input based on the position it would like to move. From there it would randomly generate an integer rather than select on like a user would. It would then move around the map based on the auto generated integer sequence. This offers the game experience to be less predictable and offer a challenge to the user who is manually inputting to move around the map based on their judgement. By having the player movement be controlled automatically it enables the game to be a bit more dynamic and engaging for the overall user.

The AI Journal component enables the system to create a journal entry based on which city they have traveled to. The system will recognize the city they are in and generate an entry about their time spent and the experience the player had while being that position. This offers more of a realistic attribution to the game offering more engagement to the story and progress of how well the player does through the game. By implementing the journal entry, the system is able to offer the user a reflection of each of their movements through the map. Creates a more interactive experience for the user without them having to manually configure the game. 


Lessons Learned: 

Working with Artificial Intelligence Aspects this semester helped me understand the quality of data that is needed to go into systems to ensure the program is running as efficiently as possible. When trying to automate it can be often difficult to accomdate for every error exception that might occur but I think with how far Artificial Intelligence has come we can often use it as a tool to guide us instead of creating something to full depend on. I think understanding how data interpretation is handled in Artificial Intelligence is one of the most important aspects and the ability for the machine to interpret what is occurring and what issues the developer wants the system to solve. In this semester alone I was able to get an idea of how intelligent agents can work in games as gaming has been around for decades and it is interesting to see how automated most of it is. This class helped me get a grasp of how artificial intelligents can work in a different variety and how we can take advantage of it ourselves. 


Appendix: 

Trying to understand how to generate a journal entry: 

Chat Log:

The first step is to import the necessary libraries, including PyTorch and the transformers library, which provides access to the pre-trained GPT-2 model and tokenizer.

Then, the GPT2Tokenizer is loaded from the pre-trained 'gpt2' tokenizer. This tokenizer is used to convert the prompt text into numerical input IDs that the model can process.

The GPT2LMHeadModel is also loaded from the pre-trained 'gpt2' model, which is a language model that can generate text given a prompt.

Next, the program checks if a CUDA-enabled GPU is available and sets the device to run on either the GPU or CPU.

The generate_journal_entry function is defined with the city_name parameter as input. The prompt variable is initialized with the input city name as part of a sentence indicating the arrival in the city. The prompt is then converted to input IDs using the pre-trained tokenizer, and the resulting tensor is moved to the device (GPU or CPU).

Trying to understand how Pytorch is used to generate the entry: 

The GPT2LMHeadModel class from the transformers library is a pre-trained neural network model that is capable of generating text based on a given prompt. We load this pre-trained model using model = GPT2LMHeadModel.from_pretrained('gpt2').

We then use the generate method of the GPT2LMHeadModel class to generate text based on a given prompt. In the code provided, we pass the input prompt "I arrived in {city_name} today." to the tokenizer.encode method to convert it to a list of numerical tokens, which is then passed to the generate method of the GPT2LMHeadModel class to generate the journal entry.

The generate method uses the pre-trained neural network model to generate a sequence of tokens based on the given input prompt. The max_length parameter specifies the maximum length of the generated sequence, and the do_sample parameter indicates whether to use sampling to generate the sequence.


Trying to understand how to restrict player movement if path does not exist:

Chat Log: 

To check if a path exists between the player's current location and their desired destination, you can run the A* algorithm on the graph, starting from the player's current location and attempting to reach the desired destination. If a path is found, the player can move along that path. If no path is found, the player's movement can be restricted.


Trying to calculate Travel cost

Chat Log:

Calculating travel cost between routes in a 2D game map that takes into account terrain can be achieved using a pathfinding algorithm that considers the terrain types and associated movement costs. One popular algorithm for this purpose is the A* (A-star) algorithm.

To use the A* algorithm, you need to represent your game map as a graph, where the nodes represent locations on the map and the edges represent the possible paths between locations. Each edge is assigned a weight, which represents the movement cost associated with traveling along that edge.

To take terrain into account, you can assign different weights to the edges depending on the terrain type. For example, moving through a forest might be slower than moving through a plain, so the weight of edges through forests can be higher than those through plains.


Sample auto generation from output from agent_environment: 


Journal entry: I arrived in Numensari today.  I had no idea I needed to stay all night, but I came out just before dawn.  I asked my dad what he was thinking, and he said I should come.  It was a cool day and I was glad everything was going well.  It turns out when I do a bit of work, people will usually come by and tell me how much I'm doing, about my book launch, and just ask about my other project.  I have had my share of requests for my book.  I am an open book owner myself and this is an unusual situation.  When I wrote My God Will, I was in a few months late.  I figured if I just kept it close to the surface and just opened to it, it would have given the story a more meaningful edge.  I think that's a good thing.  I am very excited that things are beginning to

Travelling from 5 to 7