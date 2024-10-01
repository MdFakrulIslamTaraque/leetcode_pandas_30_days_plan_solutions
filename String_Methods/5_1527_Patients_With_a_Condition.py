import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    
    #The \b in the pattern is a word boundary assertion that ensures 'DIAB1' is a separate word and not part of another word.
    diab_patients = pd.Series(patients['conditions'].str.findall(r"\b(DIAB1)"))
    patients['diab_pat_flag'] = diab_patients
    return patients[patients['diab_pat_flag'].str.len() >= 1][['patient_id', 'patient_name', 'conditions']]