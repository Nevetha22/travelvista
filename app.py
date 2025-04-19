import tornado.ioloop
import tornado.web
import os

# Mock function to simulate LLM response
def generate_itinerary(destination, trip_type, days, budget):
    return f"""
    🗺️ Here's your custom itinerary:
    
    Destination: {destination.title()}
    Trip Type: {trip_type.title()}
    Days: {days}
    Budget: {budget.title()}

    Day 1: Arrival and relax at a scenic spot 🌅  
    Day 2: Explore local attractions and hidden gems 🌟  
    Day 3: Adventure activity (tailored to trip type) 🧗‍♂️  
    Day 4: Cultural experience and food tour 🍜  
    Day 5: Relaxation or shopping 🛍️  
    Day {days}: Wrap up and fly back ✈️

    Have a great trip! 🌍
    """

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class ItineraryHandler(tornado.web.RequestHandler):
    def post(self):
        destination = self.get_body_argument("destination")
        trip_type = self.get_body_argument("tripType")
        days = int(self.get_body_argument("days"))
        budget = self.get_body_argument("budget")

        itinerary = generate_itinerary(destination, trip_type, days, budget)
        self.render("itinerary.html", itinerary=itinerary)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/itinerary", ItineraryHandler),
    ],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
