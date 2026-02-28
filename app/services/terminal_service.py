# यह फाइल शिव एआई को सिस्टम कमांड्स चलाने की अनुमति देती है
import os
import subprocess

class TerminalControl:
    def execute_command(self, cmd):
        # टर्बो स्पीड पर कमांड रन करना
        try:
            result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            return result.decode('utf-8')
        except Exception as e:
            return f"बग मिला: {str(e)}"

# कोडिंग एजेंट का हाथ तैयार
terminal_port = TerminalControl()

