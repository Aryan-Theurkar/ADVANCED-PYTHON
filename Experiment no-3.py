from functools import wraps


# Decorator to format report display
def display_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("\n" + "-" * 50)
        print("           REPORT MANAGEMENT SYSTEM")
        print("-" * 50)

        result = func(*args, **kwargs)

        print("-" * 50)
        return result

    return wrapper


class Report:

    default_title = "General Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Magic Method
    def __str__(self):
        return f"\nReport Title : {self.title}\nReport Content : {self.content}"

    # Magic Method
    def __len__(self):
        return len(self.content)

    # Class Method
    @classmethod
    def create_default_report(cls):
        return cls(cls.default_title, "This is a sample default report.")

    # Decorated Method
    @display_decorator
    def show(self):
        print(self)


def main():

    report_list = []

    while True:

        print("\n========== REPORT MENU ==========")
        print("1. Add New Report")
        print("2. Add Default Report")
        print("3. View All Reports")
        print("4. View Report Length")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            title = input("Enter Report Title: ")
            content = input("Enter Report Content: ")

            new_report = Report(title, content)
            report_list.append(new_report)

            print("\nNew Report Added Successfully!")

        elif choice == "2":

            new_report = Report.create_default_report()
            report_list.append(new_report)

            print("\nDefault Report Added Successfully!")

        elif choice == "3":

            if not report_list:
                print("\nNo reports found.")

            else:

                for number, report in enumerate(report_list, start=1):
                    print(f"\nReport {number}")
                    report.show()

        elif choice == "4":

            if not report_list:
                print("\nNo reports found.")

            else:

                for number, report in enumerate(report_list, start=1):
                    print(
                        f"\nReport {number} contains "
                        f"{len(report)} characters."
                    )

        elif choice == "5":

            print("\nThank You for using Report Management System!")
            break

        else:

            print("\nInvalid choice! Please select again.")


if __name__ == "__main__":
    main()
