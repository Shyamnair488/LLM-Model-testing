import subprocess


def query_llama3(query):
    try:
        query = f"Answer in short (minimum 100 words): {query}"   # Change the word limit of your prompt according to your intrest
        # Start the process
        process = subprocess.Popen(
            ["ollama", "run", "llama3.0:70b"], 
            stdin=subprocess.PIPE, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            encoding='utf-8'  # Explicitly set encoding to UTF-8
        )
        
        # Send the query to the process
        output, errors = process.communicate(input=query)
        
        # Print the output and errors (optional)
        if output:
            return output
        
        
        else:
            return errors
        
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return None, str(e)
    
    
if __name__ == '__main__':

    while True:
        print('What do you want to search')                
        query = input("Enter your query: ")
        if(query=="exit"):
            break
        else:
            response = query_llama3(query)
            print(response)
# --------------------