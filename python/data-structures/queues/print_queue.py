from queues import Queue as PrintQueue


class Job:
    def __init__(self, pages) -> None:
        self._pages = pages

    def print_page(self):
        if self._pages > 0:
            self._pages -= 1

    def check_complete(self):
        if self._pages == 0:
            return True
        return False


class Printer:
    def __init__(self) -> None:
        self._current_job = None

    def get_job(self, queue):
        try:
            self._current_job = queue.dequeue()
        except IndexError:
            return "All jobs complete"

    def print_job(self, job):
        while job._pages > 0:
            job.print_page()

        if job.check_complete():
            return "Printing complete"
####


first_job = Job(pages=10)
printer_queue = PrintQueue()
printer = Printer()

printer_queue.enqueue(first_job)
print(printer_queue._items)

printer.get_job(printer_queue)
# print(printer_queue._items)

print(printer.print_job(printer._current_job))
