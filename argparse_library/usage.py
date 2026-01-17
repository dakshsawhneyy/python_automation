import argparse

parser = argparse.ArgumentParser(description="EC2 Manager")
parser.add_argument("--instance-id", type=str, required=True)
parser.add_argument("--region", type=str, default="us-east-1", required=False)
parser.add_argument("--dry-run", required=False, action="store_true")

args = parser.parse_args()

print(args.dry_run)  # Either True or False

print(f"Stopping instance {args.instance_id} in region {args.region}...")
