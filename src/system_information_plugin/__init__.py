"""This is a system information plugin for Auto-GPT."""
from auto_gpt_plugin_template import AutoGPTPluginTemplate
import distro
import platform
from typing import Any, Dict, List, Optional, Tuple, TypedDict, TypeVar



# from abc import abstractmethod

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class SystemInformationPlugin(AutoGPTPluginTemplate):
    """
    This is a system information plugin for Auto-GPT which
    adds the system information to the prompt.
    """

    def __init__(self):
        super().__init__()
        self._name = "Auto-GPT-Plugin-SystemInfo"
        self._version = "0.1.0"
        self._description = "This is system info plugin for Auto-GPT."

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        os_info = self.get_system_info()
        if os_info:
            prompt.add_resource(
                f"Shell commands executed on {os_info}",
            )

        return prompt

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.
        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.
        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[Message]
    ) -> Optional[str]:
        """This method is called before the planning chat completion is done.
        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.
        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completion is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[Message]) -> List[Message]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            List[Message]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[Message]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[Message]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self, messages: Dict[Any, Any], model: str, temperature: float, max_tokens: int
    ) -> bool:
        """This method is called to check that the plugin can
          handle the chat_completion method.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
          Returns:
              bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self, messages: List[Message], model: str, temperature: float, max_tokens: int
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (List[Message]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        pass

    def get_system_info(self) -> str:
        """
        Gets system information.

        Returns:
            str: The system information.
        """

        # Get system architecture
        arch = platform.architecture()[0]

        # Get system distribution (works on Linux only)
        if platform.system() == "Linux":
            distro_name = distro.name()
            distro_version = distro.version()
            distro_id = distro.id()

            distro_info = f"{distro_name} {distro_version} ({distro_id})"
        else:
            distro_info = None

        # Get Windows version (works on Windows only)
        if platform.system() == "Windows":
            win_ver = platform.win32_ver()
            win_version = f"{win_ver[0]} {win_ver[1]} {win_ver[4]}"
        else:
            win_version = None

        # Get macOS version (works on macOS only)
        if platform.system() == "Darwin":
            mac_ver = platform.mac_ver()
            mac_version = f"{mac_ver[0]} {mac_ver[2]}"
        else:
            mac_version = None

        # Build the prompt
        if distro_info:
            os_info = f"Linux {arch} {distro_info}"
        if win_version:
            os_info = f"Windows {win_version}"
        if mac_version:
            os_info = f"macOS {mac_version}"

        return os_info
