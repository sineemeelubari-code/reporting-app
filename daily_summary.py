def main():
    print("Starting daily summary report...")

    try:
        # Your existing logic to generate and send the daily summary
        # Example: send_email(daily_summary_content)

        print("Daily report sent successfully!")

    except Exception as e:
        # Capture any error and print it to the GitHub Actions logs
        print("❌ Error while sending daily report:", str(e))

if __name__ == "__main__":
    main()
