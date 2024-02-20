from pydantic import BaseModel, Field

class Account(BaseModel):
    passphrase: str

    salt: str
    initial_vectors: str

class Store(BaseModel):
    keyhash: str
    accounts: dict[str, Account] = Field(default_factory=dict)
