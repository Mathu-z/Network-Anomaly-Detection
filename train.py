import pandas as pd
import joblib

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
# NSL-KDD column names
columns = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes",
    "land","wrong_fragment","urgent","hot","num_failed_logins",
    "logged_in","num_compromised","root_shell","su_attempted","num_root",
    "num_file_creations","num_shells","num_access_files",
    "num_outbound_cmds","is_host_login","is_guest_login","count",
    "srv_count","serror_rate","srv_serror_rate","rerror_rate",
    "srv_rerror_rate","same_srv_rate","diff_srv_rate",
    "srv_diff_host_rate","dst_host_count","dst_host_srv_count",
    "dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
    "dst_host_serror_rate","dst_host_srv_serror_rate",
    "dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "label","difficulty"
]

# Load datasets
train = pd.read_csv("dataset/KDDTrain+.txt", names=columns)
test = pd.read_csv("dataset/KDDTest+.txt", names=columns)

print(train.head())

print("\nColumns:\n")
print(train.columns)
# Convert labels into binary classes
train["label"] = train["label"].apply(
    lambda x: 0 if x == "normal" else 1
)

test["label"] = test["label"].apply(
    lambda x: 0 if x == "normal" else 1
)

print("\nLabel counts (Training):")
print(train["label"].value_counts())


# Encode protocol_type
protocol_encoder = LabelEncoder()
train["protocol_type"] = protocol_encoder.fit_transform(train["protocol_type"])
test["protocol_type"] = protocol_encoder.transform(test["protocol_type"])

# Encode service
service_encoder = LabelEncoder()
train["service"] = service_encoder.fit_transform(train["service"])
test["service"] = service_encoder.transform(test["service"])

# Encode flag
flag_encoder = LabelEncoder()
train["flag"] = flag_encoder.fit_transform(train["flag"])
test["flag"] = flag_encoder.transform(test["flag"])

print("\nProtocol Mapping:")
for protocol, value in zip(protocol_encoder.classes_, range(len(protocol_encoder.classes_))):
    print(f"{protocol} -> {value}")

print("\nService Mapping:")
for service, value in zip(service_encoder.classes_, range(len(service_encoder.classes_))):
    print(f"{service} -> {value}")

print("\nFlag Mapping:")
for flag, value in zip(flag_encoder.classes_, range(len(flag_encoder.classes_))):
    print(f"{flag} -> {value}")

# Select features and target
features = [
    "duration",
    "protocol_type",
    "service",
    "flag",
    "src_bytes",
    "dst_bytes",
    "count",
    "srv_count",
    "logged_in",
    "serror_rate"
]

X_train = train[features]
y_train = train["label"]

X_test = test[features]
y_test = test["label"]

print("\nSelected Features:")
print(X_train.head())

print("\nTarget:")
print(y_train.head())



# Create the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy: {accuracy:.2%}")
# Save the trained model
joblib.dump(model, "models/network_model.pkl")

# Save the encoders
joblib.dump(protocol_encoder, "models/protocol_encoder.pkl")
joblib.dump(service_encoder, "models/service_encoder.pkl")
joblib.dump(flag_encoder, "models/flag_encoder.pkl")

print("\nModel saved successfully!")