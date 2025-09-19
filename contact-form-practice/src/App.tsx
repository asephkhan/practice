function App() {
  return (
    <div className="flex items-center justify-center bg-green-200 p-4">
      <form className=" bg-white w-full max-w-2xl flex-col justify-center rounded-md p-6 ">
        <h1 className="font-sans text-h1 pb-32px">Contact Us</h1>
        {/* fields */}
        {/* first name and last name */}
        <div className="gap-6 flex flex-col md:flex-row ">
          <div className="flex flex-1 flex-col gap-2 ">
            <label htmlFor="firstName" className="font-sans text-body-sm ">First Name *</label>
            <input
              type="text"
              id="firstName"
              name="firstName"
              value={''}
              required
              className="rounded-md border px-24px py-12px border-grey-500 hover:border-grey-900"
            />
          </div>
          <div className="flex flex-1 flex-col text-body-sm gap-2  ">
            <label className="font-sans ">Last Name *</label>

            <input
              type="text"
              required
              className="rounded-md border px-24px py-12px border-grey-500 hover:border-grey-900"
            />
          </div>
        </div>
        {/* email adress */}
        <div className="flex flex-col gap-8px pt-24px">
          <label>Email Adress *</label>
          <input
            type="text"
            required
            className=" px-24px py-12px border border-grey-500 rounded-md hover:border-grey-900"
          />
        </div>
        {/* query type */}

        <div className="pt-6 pb-4">
          <label>Query Type *</label>
        </div>
        <div className="flex flex-col gap-6 md:flex-row ">
          <label className="flex flex-1 items-center gap-2.5 border border-grey-500 rounded-md px-4 py-12px hover:border-grey-900 ">
            <input className=""  type="radio" />
            General Enquiry
          </label>

          <label className="flex flex-1 items-center gap-2.5 border border-grey-500 rounded-md px-4 py-12px hover:border-grey-900  ">
            <input className="" type="radio"></input>
            Support Request
          </label>
        </div>

        {/* message */}
        <div className="flex flex-col gap-8px pt-24px">
          <label>Message *</label>

          <textarea
            id="message"
            rows={6}
            
            className="border border-grey-500 rounded-md px-24px py-12px gap-16px hover:border-grey-900"
          ></textarea>
        </div>
        {/* consent check box */}
        <div className="flex items-center gap-16px py-24px">
          <input className="" type="checkbox"/>
          <label className="text-body-s text-grey-900">I consent to being contacted by the team</label>
        </div>
        {/* button */}
        <div>
          <button type="submit" className="bg-green-600 rounded-md py-4 w-full text-white text-body-md ">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}

export default App;
