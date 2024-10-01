import pandas as pd

"""
                                        Regex basics
                                    --------------------
[]  : A set of characters,                                                          e.g.-->"[a-m]"	
\   : Signals a special sequence (can also be used to escape special characters)    e.g.-->	"\d"	
.	: Any character (except newline character)	                                    e.g.-->"he..o"	
^	: Starts with                                                                   e.g.-->"^hello"	
$	: Ends with	                                                                    e.g.-->"planet$"	
*	: Zero or more occurrences	                                                    e.g.--> "he.*o"	
+	: One or more occurrences	                                                    e.g.-->"he.+o"	
?	: Zero or one occurrences	                                                    e.g.-->"he.?o"	
{}	: Exactly the specified number of occurrences	                                e.g.-->"he.{2}o"	
|	: Either or	                                                                    e.g.-->"falls|stays"	
()	: Capture and group

"""

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.fullmatch(r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$") == True]