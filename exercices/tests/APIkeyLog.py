from qiskit_ibm_runtime import QiskitRuntimeService

QiskitRuntimeService.save_account(
token="hehehe", # Use the 44-character API_KEY you created and saved from the IBM Quantum Platform Home dashboard
instance="<CRN>", # Optional
)


from qiskit_ibm_runtime import QiskitRuntimeService

# The credentials you enter will override any saved
# account credentials that might be available locally.
service = QiskitRuntimeService(
  # Use the 44-character API_KEY you created and saved from
  # the IBM Quantum Platform dashboard, and then delete
  # the key on the API keys page after entering this code:
  token="<your-API-key>", 
  
  # Optionally specify an instance to use
  instance="<IBM Cloud CRN or instance name>"
  )