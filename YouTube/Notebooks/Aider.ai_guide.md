# Aider AI Tool - Comprehensive Guide (2025 Edition)

## Introduction

Aider is a powerful AI-powered pair programming tool that integrates with your local git repository, allowing developers to collaborate with Large Language Models (LLMs) directly from their terminal. It enables you to manage, edit, and refactor code within your local Git repositories by leveraging AI capabilities to make complex code changes, fix bugs, and handle multi-file projects.

Aider works with most popular programming languages including Python, JavaScript, Rust, Ruby, Go, C++, PHP, HTML, CSS, and many others. The tool is particularly valuable for developers working on large codebases who want to streamline their coding workflow and boost productivity.

### Supported Models

Aider works best with:
- Claude 3.7 Sonnet
- DeepSeek R1 & Chat V3
- OpenAI o1 and o3-mini
- GPT-4o

However, it can connect to almost any LLM, including local models.

## Prerequisites

Before using Aider, ensure you have the following:

- A stable internet connection
- A local git repository
- Python installed (version 3.8-3.13 recommended)
- Access to an API key for your preferred LLM

## Step 1: Install Aider

### Basic Installation

1. Open a terminal window.
2. Install Aider using the recommended installer:
   ```sh
   python -m pip install aider-install
   aider-install
   ```

3. Verify the installation:
   ```sh
   aider --version
   ```

### Alternative Installation Methods

If you prefer, you can use other installation methods:

#### Using pipx (for Python 3.9-3.12)
```sh
pipx install aider-chat
```

#### Using pip directly
```sh
python -m pip install -U --upgrade-strategy only-if-needed aider-chat
```

#### Using Docker
```sh
docker pull paulgauthier/aider
docker run -it --volume $(pwd):/app paulgauthier/aider --openai-api-key $OPENAI_API_KEY
```

## Step 2: Set Up Your Git Repository

1. Navigate to your project directory:
   ```sh
   cd /path/to/your/project
   ```

2. Ensure git is initialized:
   ```sh
   git init
   ```

3. Connect to a remote repository (optional):
   ```sh
   git remote add origin <your-repo-url>
   ```

4. Make sure your working directory is clean:
   ```sh
   git status
   ```

## Step 3: Start Aider

### Basic Startup

1. Run Aider in your terminal with your preferred model:

   #### For Claude 3.7 Sonnet:
   ```sh
   aider --model sonnet --api-key anthropic=<your-anthropic-key>
   ```

   #### For OpenAI's o3-mini:
   ```sh
   aider --model o3-mini --api-key openai=<your-openai-key>
   ```
   
   #### For DeepSeek:
   ```sh
   aider --model deepseek --api-key deepseek=<your-deepseek-key>
   ```

2. If you've set your API key as an environment variable, you can simply use:
   ```sh
   aider --model sonnet
   ```

### Advanced Startup Options

To use a specific chat mode at startup:
```sh
aider --chat-mode architect
```

For multiline input mode:
```sh
aider --multiline
```

To enable voice commands:
```sh
aider --voice
```

## Step 4: Working with Files

### Adding Files to Chat

1. At startup, specify the files you want to edit:
   ```sh
   aider your_script.py app.js
   ```

2. Or add files during the chat session:
   ```
   /add another_file.py config.json
   ```

3. Check which files are currently in the chat:
   ```
   /files
   ```

### Example: Adding a Feature to an Existing File

Let's say you want to add a factorial function to a Python math utility file:

1. Add the file to the chat:
   ```sh
   aider math_utils.py
   ```

2. Request the new feature:
   ```
   Add a factorial function that can handle numbers from 0 to 20 and raises a ValueError for negative inputs or inputs greater than 20.
   ```

3. Aider will suggest changes, showing a diff of what it plans to modify.

4. Review the changes, and they'll be automatically applied to your file and committed to git.

## Step 5: Chat Modes and Commands

Aider offers different chat modes to help you work more effectively:

### Chat Modes

1. **Code Mode** (`/code`) - Default mode for making code changes
2. **Ask Mode** (`/ask`) - Discussion mode that doesn't modify files
3. **Architect Mode** (`/architect`) - Plan changes before implementation
4. **Help Mode** (`/help`) - Get assistance with Aider

### Essential Commands

| Command | Description |
|---------|-------------|
| `/add <files>` | Add files to the chat |
| `/drop <files>` | Remove files from the chat |
| `/files` | List files in the chat |
| `/run <command>` | Run a shell command and show output |
| `/clear` | Clear the chat history |
| `/model <model-name>` | Switch to a different LLM |
| `/tokens` | Show token usage |
| `/help` | Get help with commands |

### Using Voice Commands

You can use your voice to instruct Aider through the `/voice` command:

1. Type `/voice` in the chat
2. Speak your instructions clearly
3. Press ENTER when done
4. Your speech will be transcribed and processed as a text command

#### Example Voice Workflow

```
/voice
[Speak: "Add a function to calculate the nth Fibonacci number using recursion"]
[Press ENTER]
```

Aider will then implement the requested feature.

## Step 6: Advanced Features

### Working Across Multiple Files

Aider excels at making coordinated changes across multiple files. Here's an example workflow:

1. Add all relevant files:
   ```sh
   aider models.py views.py templates/index.html
   ```

2. Request a change that spans these files:
   ```
   Add a new "User Profile" feature that includes a model field for bio, a view method to display it, and update the template to show the bio on the user profile page.
   ```

3. Aider will make coordinated changes across all three files.

### Using Different Chat Modes Together

A recommended workflow is to bounce between `/ask` and `/code` modes:

1. Start in ask mode to discuss options:
   ```
   /ask What's the best way to implement pagination for my user list?
   ```

2. After discussing the approach, switch to code mode:
   ```
   /code
   ```

3. Request the implementation:
   ```
   Implement the pagination using the approach we discussed.
   ```

### Debugging with Aider

When your code has errors, Aider can help fix them:

1. Run your code and capture the error:
   ```
   /run python app.py
   ```

2. Ask Aider to fix the issue:
   ```
   Fix the error shown in the output.
   ```

3. Aider will analyze the error and suggest corrections.

### Web URL Integration

Aider can incorporate documentation or references from the web:

1. Simply paste a URL into the chat:
   ```
   https://docs.python.org/3/library/collections.html
   ```

2. Aider will scrape the content and use it as reference for your requests.

### Using AI Comments in Your Editor

Aider can watch your files for "AI comments" that you add in your code editor:

1. Start Aider in watch mode:
   ```sh
   aider --watch
   ```

2. Add comments to your code that start with specific prefixes:
   
   ```python
   def calculate_total(items):
       # ai: Add validation for empty list and negative prices
       total = 0
       for item in items:
           total += item['price']
       return total
   ```

3. Save the file, and Aider will detect the comment and make the requested changes.

## Step 7: Git Integration

Aider automatically commits changes to your git repository:

1. Each set of changes is committed with a descriptive message
2. View the commit history:
   ```sh
   git log
   ```

3. Revert changes if needed:
   ```sh
   git revert <commit-hash>
   ```

4. You can disable auto-commits if preferred:
   ```sh
   aider --no-auto-commits
   ```

## Step 8: Customization and Configuration

### Configuration Files

Create a `.aider.conf.yml` file in your project or home directory for persistent configuration:

```yaml
# .aider.conf.yml
model: sonnet
api_key: anthropic=your_key_here
dark_mode: true
auto_commits: true
```

### Environment Variables

You can set various environment variables to configure Aider:

```sh
export AIDER_MODEL=sonnet
export ANTHROPIC_API_KEY=your_key_here
```

### Command-Line Options

Aider supports numerous command-line options to customize behavior:

```sh
aider --dark-mode --multiline --stream --chat-mode ask
```

## Step 9: Troubleshooting

### Common Issues and Solutions

1. **"Command not found" error**:
   - Use `python -m aider` instead
   - Check your PATH environment variable

2. **API Key Issues**:
   - Verify key is correct
   - Check environment variables
   - Use `--api-key service=key` format

3. **Performance Issues**:
   - Try a different model
   - Reduce the number of files in the chat
   - Use `/drop` to remove unused files

### Debug Mode

If Aider isn't working as expected, use debug mode:

```sh
aider --verbose
```

### Getting Help

1. Use the built-in help:
   ```
   /help
   ```

2. For specific help topics:
   ```
   /help voice
   /help models
   ```

## Step 10: Real-World Examples

### Example 1: Creating a FastAPI Backend

Let's use Aider to create a simple FastAPI backend:

1. Initialize a new directory:
   ```sh
   mkdir fastapi-demo && cd fastapi-demo
   git init
   ```

2. Start Aider:
   ```sh
   aider --model sonnet
   ```

3. Create a new FastAPI app:
   ```
   Create a FastAPI application with endpoints for listing, creating, updating, and deleting todo items. Include proper validation, error handling, and a SQLite database for storage.
   ```

4. Test the implementation:
   ```
   /run pip install fastapi uvicorn sqlalchemy
   /run uvicorn main:app --reload
   ```

### Example 2: Refactoring Legacy Code

Using Aider to refactor legacy code:

1. Start Aider with your legacy code:
   ```sh
   aider old_script.py
   ```

2. Request a refactoring:
   ```
   This code uses outdated Python 2 style syntax and doesn't follow PEP 8. Refactor it to use modern Python 3 practices, add type hints, and organize it into proper classes and functions.
   ```

3. Review the changes and approve them.

### Example 3: Implementing Test Cases

Creating comprehensive tests for existing code:

1. Add both your code and empty test file:
   ```sh
   aider user_auth.py test_user_auth.py
   ```

2. Request test implementation:
   ```
   Write comprehensive unit tests for the user_auth.py module. Include tests for normal operations, edge cases, and error handling. Use pytest fixtures where appropriate.
   ```

## Conclusion

Aider AI is a powerful tool that brings the capabilities of AI-assisted coding directly to your terminal. By reducing manual effort, automating repetitive tasks, and providing intelligent coding assistance, it can significantly boost your productivity as a developer.

The combination of Aider's terminal-based interface, git integration, and support for various LLMs makes it an excellent choice for developers who want to leverage AI in their workflow without disrupting their existing development practices.

As AI coding assistants continue to evolve, tools like Aider represent the future of development—where human creativity and problem-solving skills are augmented by AI's ability to handle routine coding tasks and suggest improvements.

## Additional Resources

- [Official Aider Documentation](https://aider.chat/docs/)
- [GitHub Repository](https://github.com/Aider-AI/aider)
- [Aider Discord Community](https://discord.gg/aider)

---

*This guide was last updated in May 2025.*
